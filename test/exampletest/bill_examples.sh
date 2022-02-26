#!/bin/sh

script=`basename "$0"`

do_help() {
    error=$*

    echo "${script}: Test example scripts in a path"
    echo ""
    echo "Usage: ${script} input command"
    echo "\tinput\t Directory to find all files *.bill to test"
    echo "\tcommand\t Command to test each *.bill file with as the only argument"
    echo ""
    echo "Runs each file *.bill found in path as: command file"
    echo "If the command fails (returns non 0) it is listed as an error."
    echo "This script returns the count of failed tests, or 0 for success."

    if [ -n "${error}" ] ; then
	echo ""
	echo "Error: ${error}"
	exit 1
    else
	exit 0
    fi
}

input=$1
command=$2

if [ -z "${input}" -a -z "${command}" ] ; then
    do_help
fi

if [ "${input}" = "-h" -o "${input}" = "--help" ] ; then
    do_help
fi

if [ ! -d "${input}" ] ; then
    do_help "Failed to find test directory: \"${input}\""
fi

if [ -z "${command}" ] ; then
    do_help "Missing command"
fi

examples=`find ${input} -name *.bill`
continue=1
run=0
failed=0

if [ -z "${examples}" ] ; then
    do_help "No tests found in path: \"${input}\""
fi

echo "Example Test: Testing all in \"${input}\" with \"${command}\""

for file in ${examples} ; do
    run=$((run+1))
    ${command} ${file}
    result=$?
    if [ 0 -ne ${result} ] ; then
	echo "FAILED: \"${command} ${file}\" returned ${result}"
	failed=$((failed+1))
	if [ 0 -eq ${continue} ] ; then
	    exit 1
	fi
    fi
done

if [ 0 -ne ${failed} ] ; then
    echo "Example Test: Complete with failures: Ran ${run} Failed ${failed}"
    exit ${failed}
else
    echo "Example Test: All Tests passed: Ran ${run}"
    exit 0
fi
