#!/bin/bash
# 在各书的 view/ 子目录下执行本脚本，创建 all_pics.tex 文件。
# 如： 在 chuzhong-daishu-1/view/ 目录下，执行
#     ../../create_all_pics.sh
ls ../pic/*.tex | awk '{printf "\\input{%s}\n\n%s\n\n", $1, $1}' > all_pics.tex
