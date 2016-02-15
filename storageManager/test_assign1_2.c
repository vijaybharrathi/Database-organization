#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include "storage_mgr.h"
#include "dberror.h"
#include "test_helper.h"

// test name
char *testName;

/* test output files */
#define TESTPF "test_pagefile.bin"

/* prototypes for test functions */

static void testSinglePageContent(void);

/* main function running all tests */
/* main function running all tests */
int main(void) {
	testName = "";

	initStorageManager();
	testSinglePageContent();
	return 0;
}

void testSinglePageContent(void) {
	SM_FileHandle fh;
	SM_PageHandle ph;
	int i;

	testName = "test single page content";

	ph = (SM_PageHandle) malloc(PAGE_SIZE);


	TEST_CHECK(createPageFile (TESTPF));
	TEST_CHECK(openPageFile (TESTPF, &fh));
	printf("created and opened file\n");


	TEST_CHECK(readFirstBlock(&fh, ph));


	for (i = 0; i < PAGE_SIZE; i++)
		ASSERT_TRUE((ph[i] == 0),
				"expected zero byte in first page of freshly initialized page");
	printf("first block was empty\n");


	for (i = 0; i < PAGE_SIZE; i++)
		ph[i] = (i % 10) + '0';
	TEST_CHECK(writeBlock(0, &fh, ph));


	TEST_CHECK(writeCurrentBlock(&fh, ph));
	TEST_CHECK(appendEmptyBlock(&fh));
	TEST_CHECK(readBlock(0, &fh, ph));
	TEST_CHECK(readLastBlock(&fh, ph));
	TEST_CHECK(readCurrentBlock(&fh, ph));
	TEST_CHECK(ensureCapacity(100, &fh));

	printf("writing first block\n");


	TEST_CHECK(readFirstBlock(&fh, ph));
	for (i = 0; i < PAGE_SIZE; i++)
		ASSERT_TRUE((ph[i] == (i % 10) + '0'),
				"character in page read from disk is the one we expected.");
	printf("reading first block\n");


	printf("end---");
	TEST_CHECK(destroyPageFile (TESTPF));

	TEST_DONE()
	;
}

