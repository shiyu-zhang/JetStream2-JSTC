# Copyright (C) 2017 Apple Inc. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY APPLE INC. ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE INC. OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# This converts an offline assembly file into a JavaScript string.
# It adds newline escapes and properly escapes double quote (") characters.
# The input and output files are specified on the command line.
#
# Example:
#     python convert_asm_to_js.py LowLevelInterpreter.asm LowLevelInterpreter.js

import argparse
import re


headerText = """/*
 * DO NOT EDIT THIS FILE, it is autogenerated.
 */
"use strict";

"""


def convertFile(inputFile, outputFile):
    outputFile.write(headerText)
    outputFile.write("(function() {\n")
    outputFile.write("    let source = `")
    for line in inputFile:
        line = re.sub("`", "\\`", line);
        outputFile.write(line)

    outputFile.write("`;\n")
    outputFile.write("\n")
    outputFile.write("    new File(\"{fileName}\", source);\n".format(fileName=inputFile.name))
    outputFile.write("})();\n")
    outputFile.write("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("inputFile", type = argparse.FileType('r'), help="Offline Assembler input file")
    parser.add_argument("outputFile", type = argparse.FileType('w'), help="JavaScript output file")
    args = parser.parse_args()

    convertFile(args.inputFile, args.outputFile)
