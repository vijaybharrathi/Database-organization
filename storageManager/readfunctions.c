#include<stdio.h>
#include "storage_mgr.c"

RC readBlock (int pageNum, SM_FileHandle *fHandle, SM_PageHandle memPage)
{

FILE *fp;
fp = fopen(fHandle->fileName,"r");
if (fp==NULL)
{
	return RC_FILE_NOT_FOUND
} 
else 
{

	if ( pageNum > fHandle->totalNumPages )
	{
		return RC_READ_NON_EXISTING_PAGE;
	}

	else
	{
		int status=fseek(fp,pageNum*PAGE_SIZE,SEEK_SET)
		if(status==0)
		{
			fread(memPage,PAGE_SIZE,1,fp)
			fHandle->curPagePos = pageNum
			return RC_OK;
		}
		else
		{
			return RC_READ_NON_EXISTING_PAGE;
		}

}
}

RC readFirstBlock (SM_FileHandle *fHandle, SM_PageHandle memPage)
{
	readBlock(0,fHandle,memPage)
}

RC readPreviousBlock (SM_FileHandle *fHandle, SM_PageHandle memPage)
{

	int previousBlock = getBlockPos(fHandle) - 1;
        readBlock(previousBlock,fHandle,memPage);
}

RC readCurrentBlock (SM_FileHandle *fHandle, SM_PageHandle memPage)
{
	int currentBlock = getBlockPos(fHandle);
	readBlock(currentBlock,fHandle,memPage);
}
RC readNextBlock (SM_FileHandle *fHandle, SM_PageHandle memPage)
{
	int nextBlock = getBlockPos(fhandle);
	readBlock(nextBlock,fHandle,memPage);
}
RC readLastBlock (SM_FileHandle *fHandle, SM_PageHandle memPage)
{
	int lastBlock= fHandle->totalNumPages -1
	readBlock(nextBlock,fHandle,memPage);
}


 	




		 


