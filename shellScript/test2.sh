#!/bin/bash
myUrl="https://www.runoob.com"
unset myUrl
echo $myUrl

myUrl2="https://www.google.com"
readonly myUrl2
unset myUrl2
echo ${myUrl2}