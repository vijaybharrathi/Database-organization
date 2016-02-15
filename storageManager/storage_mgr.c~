#include "dberror.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include "storage_mgr.h"
#include <fcntl.h>

//test

static RC getBlock(int, SM_FileHandle *, SM_PageHandle);

/*
*	Initalize StorageManager Function
*	A simple Intialize function does not do much
*
*	@author Praveen
*	@return void 
*/
void initStorageManager(void) 
{
	printf(" Storage Manager is Intialized \n");
}
/*
*	createPageFile Function
* 	Creates a new page file fileName with one page 
*	and fills the single page with '\0' bytes.
*
*	@author Praveen
*	@return RC value(defined in dberrror.h)
*/
RC createPageFile (char *fileName)
{
	FILE *newFile;
	char *str;
	newFile=fopen(fileName,"w+");
		//Opens a text file for writing. If it does not exist,
 		//then a new file is created

	if(newFile==NULL)
		return RC_FILE_NOT_FOUND;

	//Allocates the PAGE_SIZE as memory and fills it with null
	str=malloc(PAGE_SIZE);
	memset(str,'\0',PAGE_SIZE);
	fwrite(str,PAGE_SIZE,1,newFile);
	free(str);
	return RC_OK;

	
}
/*
*	openPageFile Method
*	opens the existing pageFile and the fileHandle fields are 
*	initalized with the information about the opened file 
*
*	@author Praveen
*	@return RC value(defined in dberrror.h)
*/

RC openPageFile(char *fileName, SM_FileHandle *fHandle)
{
	FILE *newFile;
	newFile=fopen(fileName,"r");
	int fileSize;
	if(newFile==NULL)
		return RC_FILE_NOT_FOUND;
	
	if(fseek(newFile,0,SEEK_END)!=0)
		return RC_SEEK_ERROR;
	
	fileSize=ftell(newFile)/PAGE_SIZE;
	//printf("%d\n\n",fileSize);	
	fseek(newFile,0,SEEK_SET);
	fHandle->fileName=fileName;
	fHandle->curPagePos=0;
	fHandle->mgmtInfo=newFile;	
	fHandle->totalNumPages=fileSize;
	return RC_OK;
		
}

/*	closePageFile method 
*	closes an existing pageFile
*
*	@author Praveen
*	@return RC value(defined in dberrror.h)
*/
RC closePageFile (SM_FileHandle *fHandle)
{	
	if(fopen(fHandle->fileName,"r")==NULL)
		return RC_FILE_NOT_FOUND;
	if(fHandle==NULL)
		return RC_FILE_HANDLE_NOT_INIT;
	if(fclose(fHandle->mgmtInfo)==0)
		return RC_OK;
	else
		return RC_FILE_CANNOT_BE_CLOSED;
	

}

RC destroyPageFile(char *fileName) {
	if (remove(fileName) != 0) {
		printf("Error occurred in file deletion\n\n");
		return RC_FILE_DELETE_FAILED;
	}
	return RC_OK;
}

/*
 *   A static function to get nth block from the page
 *	Arguments - postion,fHandle and memPage
 *	Returns - Block that is read
 *
 */

static RC getBlock(int position, SM_FileHandle *fHandle, SM_PageHandle memPage) {

// Check if requested page is existing
	if (position > fHandle->totalNumPages && position < 0) {
		return RC_READ_NON_EXISTING_PAGE;
	}

	FILE *fileName; // Pointer to File
	fileName = fHandle->mgmtInfo;
	fflush(fileName);

	fseek(fileName, PAGE_SIZE * position, SEEK_SET); // Seek to the requested block,by moving File pointer
	fread(memPage, PAGE_SIZE, 1, fileName); // Read requested block to memPage

	return RC_OK;
}

RC readBlock(int pageNum, SM_FileHandle *fHandle, SM_PageHandle memPage) {
	fHandle->curPagePos = pageNum;
	int position = pageNum;

	if (position > fHandle->totalNumPages) //Check for existence
			{
		return RC_READ_NON_EXISTING_PAGE; //Return specifed RC value
	}

	return getBlock(position, fHandle, memPage);
}

int getBlockPos(SM_FileHandle *fHandle) {
	if (fHandle == NULL)
		return RC_FILE_HANDLE_NOT_INIT;
	else
		return fHandle->curPagePos;
}

RC readFirstBlock(SM_FileHandle *fHandle, SM_PageHandle memPage) {

	int position = 0;
	if (fHandle == NULL) //Check for existence
	{
		return RC_READ_NON_EXISTING_PAGE; //Return specifed RC value
	}

	return getBlock(position, fHandle, memPage);

}

/*
 *   To read the block previous to the block pointed by fHandle
 *	Arguments - fHandle and memPage
 *	Returns - Block that is read
 *
 */

RC readPreviousBlock(SM_FileHandle *fHandle, SM_PageHandle memPage) {
	int position = fHandle->curPagePos - 1; // Setting position to previous block from current block

	// Check if fHandle is iniatized
	if (fHandle == NULL) {
		return RC_READ_NON_EXISTING_PAGE;
	}

	return getBlock(position, fHandle, memPage);

}

/*
 *   To read the block  pointed by fHandle
 *	Arguments - fHandle and memPage
 *	Returns - Block that is read
 *
 */

RC readCurrentBlock(SM_FileHandle *fHandle, SM_PageHandle memPage) {
	int position = fHandle->curPagePos; // Setting position to current block

	// Check if fHandle is iniatized
	if (fHandle == NULL) {
		return RC_READ_NON_EXISTING_PAGE;
	}

	return getBlock(position, fHandle, memPage);
}

/*
 *   To read the block next to the block pointed by fHandle
 *	Arguments - fHandle and memPage
 *	Returns - Block that is read
 *
 */

RC readNextBlock(SM_FileHandle *fHandle, SM_PageHandle memPage) {
	int position = fHandle->curPagePos + 1; // Setting position to next block

	// Check if fHandle is iniatized
	if (fHandle == NULL || position > fHandle->totalNumPages) {
		return RC_READ_NON_EXISTING_PAGE;
	}

	return getBlock(position, fHandle, memPage);

}

/*
 *   To read the last block of the page
 *	Arguments - fHandle and memPage
 *	Returns - Block that is read
 *
 */

RC readLastBlock(SM_FileHandle *fHandle, SM_PageHandle memPage) {
	int position = fHandle->totalNumPages - 1; // Setting position to last block of the page

	// Check if fHandle is iniatized
	if (fHandle == NULL) {
		return RC_READ_NON_EXISTING_PAGE;
	}

	return getBlock(position, fHandle, memPage);
}

/*RC writeBlock(int pageNum, SM_FileHandle *fHandle, SM_PageHandle memPage)
 {
 /*  check if the file write is files*/
/* if(NULL == fHandle->mgmtInfo)
 {
 printf("\n  Error with the file!!!\n");
 return RC_WRITE_FAILED;
 }
 /* get the current position of the file pointer*/
// fseek(fHandle->mgmtInfo,PAGE_SIZE * pageNum ,0);
/* write contents to the file*/
//fwrite(memPage,PAGE_SIZE,1,fHandle->mgmtInfo);
/* Close the file*/
/* closePageFile(fHandle);
 printf("\n File stream closed through fclose()\n");
 return RC_OK;
 }*/

/**
 *This function writes a block.
 *
 *
 * @author  Smriti Raj
 * @param   SM_FileHandle(contains the current page loaction,
 *		   file name, total pages and
 *          management information),
 *          pageHandle(points to the area in memory
 *          storing the page data)
 * @return  RC value(defined in dberror.h)
 * @since   2016-07-02
 */
RC writeBlock(int pageNum, SM_FileHandle *fHandle, SM_PageHandle pageMem) {
	RC pNumValid = pageNumValid(pageNum);
	if (pNumValid != RC_OK) {
		return pNumValid;
	}

	RC fileInitValid = checkFileInit(fHandle);
	if (fileInitValid != RC_OK) {
		return fileInitValid;
	}

	printf(" Initial conditions checked writing block to page number %d",
			pageNum);

	fseek(fHandle->mgmtInfo, PAGE_SIZE * pageNum, 0);
	fwrite(pageMem, PAGE_SIZE, 1, fHandle->mgmtInfo);
	closePageFile(fHandle);
	return RC_OK;
}

/**
 *This function writes a block.
 *
 *
 * @author  Smriti Raj
 * @param   SM_FileHandle(contains the current page loaction,
 *		   file name, total pages and
 *          management information),
 *          pageHandle(points to the area in memory
 *          storing the page data)
 * @return  RC value(defined in dberror.h)
 * @since   2016-07-02
 */
RC writeCurrentBlock(SM_FileHandle *fHandle, SM_PageHandle memPage) {
	RC isFHandleInit = checkFileInit(fHandle);
	if (isFHandleInit != RC_OK) {
		return isFHandleInit;
	}
	printf("Writing current block to file :%s", fHandle->fileName);

	int position = fHandle->curPagePos;
	position = (position) * PAGE_SIZE;

	if (position < 0) {
		return RC_INVALID_POSITION;
	}
	if (-1 == (fwrite(memPage, PAGE_SIZE, 1, fHandle->mgmtInfo))) {
		return RC_WRITE_FAILED;
	} else {
		closePageFile(fHandle);
		return RC_OK;

	}

}

/**
 *This function adds an empty new block.
 *
 *
 * @author  Smriti Raj
 * @param   SM_FileHandle(contains the current page loaction,
 *		   file name, total pages and
 *          management information),
 *          pageHandle(points to the area in memory
 *          storing the page data)
 * @return  RC value(defined in dberror.h)
 * @since   2016-07-02
 */
RC appendEmptyBlock(SM_FileHandle *fHandle) {
	RC isFHandleInit = checkFileInit(fHandle);
	if (isFHandleInit != RC_OK) {
		return isFHandleInit;
	}
	//printf("We are adding an empty block to file", fHandle->fileName);
	FILE *filePointer;
	filePointer = fHandle->mgmtInfo;
	char *start;
	filePointer = fopen(fHandle->fileName, "a");
	fHandle->totalNumPages = fHandle->totalNumPages + 1;
	fseek(filePointer, (fHandle->totalNumPages * PAGE_SIZE), SEEK_END);

	start = calloc(PAGE_SIZE, sizeof(char));
	fwrite(start, PAGE_SIZE, sizeof(char), filePointer);
	closePageFile(fHandle);
	free(start);
	return RC_OK;

}

/**
 * We are ensuring the capacity of the number of pages of the file
 * @author  Smriti Raj
 * @param   SM_FileHandle(contains the current page loaction,
 *		   file name, total pages and
 *          management information),
 *          pageHandle(points to the area in memory
 *          storing the page data)
 * @return  RC value(defined in dberror.h)
 * @since   2016-07-02
 */
RC ensureCapacity(int numberOfPages, SM_FileHandle *fHandle) {
	RC isPageNumberValid = pageNumValid(numberOfPages);
	int diffPages, i;
	if (isPageNumberValid != RC_OK) {
		return isPageNumberValid;
	}

	RC isFHandleInit = checkFileInit(fHandle);
	if (isFHandleInit != RC_OK) {
		return isFHandleInit;
	}

	printf("We are ensuring the capacity of the pages %d", numberOfPages);

	if (fHandle->totalNumPages < numberOfPages) {
		diffPages = numberOfPages - fHandle->totalNumPages;
		for (i = 0; i < diffPages; i++) {
			fprintf(fHandle->mgmtInfo, "%c", '\0');
		}
	}
	return RC_OK;
}
/**
 *This function checks if the file handle is initiated.
 *
 * @author  Smriti Raj
 * @param   SM_FileHandle(contains current page position,
 *		   file name, total pages and
 *          management information)
 * @return  RC
 * @since   2016-07-02
 */
RC checkFileInit(SM_FileHandle *fHandle) {
	if (fHandle == NULL || fHandle->fileName == NULL
			|| fHandle->mgmtInfo == NULL || fHandle->totalNumPages < 0
			|| fHandle->curPagePos < 0) {
		// checks whether SM_FileHandle or the file Handle is initiated properly
		return RC_FILE_HANDLE_NOT_INITIATED;
	} else {
		return RC_OK;
	}
}

/**
 *This function checks if page number is valid.
 *
 * @author  Smriti Raj
 * @param   Page Number
 * @return  RC_OK
 * @since   2016-07-02
 */
RC pageNumValid(int pNum) {
	// check to find if page number is greater than 0
	// it is valid only if it is greater than 0
	if (pNum >= 0) {
		return RC_OK;
	} else {
		return RC_PAGENUM_INVALID;
	}

}

