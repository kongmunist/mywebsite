#!/bin/bash

BLOG_TEMPLATE_NAME="blogtemplate"
BLOG_TEMPLATE_ENDING=".md"
NUM_BLOG_POSTS=$(ls -l pages/blog/ | wc -l)
NUM_POSTS=`echo $NUM_BLOG_POSTS | sed 's/ *$//g'`

NEW_BLOG_PATH="pages/blog/${BLOG_TEMPLATE_NAME}${NUM_POSTS}${BLOG_TEMPLATE_ENDING}"

cd
cd Library/Mobile\ Documents/com~apple~CloudDocs/programming/personalwebsite
cp "${BLOG_TEMPLATE_NAME}${BLOG_TEMPLATE_ENDING}" $NEW_BLOG_PATH

open $NEW_BLOG_PATH
open pages/blog/
open static/
