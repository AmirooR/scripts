#!/bin/bash
for x in `ls *.cpp *.h`; do
#echo "$x";
nums=$(grep -iHn include\ \"cxcore $x|wc -l)
if [ $nums -ne "0" ];
then
echo "$nums"
sed s/"#include \"cxcore.h\""/"#include <opencv.hpp>"/g $x > _tmp
`cat _tmp > $x`
fi
nums=$(grep -iHn include\ \"cv.h $x|wc -l)
#nums=$(grep -iHn cv.h $x|wc -l)
if [ $nums -ne "0" ];
then
echo "$nums"
sed s/"#include \"cv.h\""/"#include <opencv.hpp>"/g $x > _tmp
`cat _tmp > $x`
fi

nums=$(grep -iHn include\ \"highgui.h $x|wc -l)
#nums=$(grep -iHn cv.h $x|wc -l)
if [ $nums -ne "0" ];
then
echo "$nums"
sed s/"#include \"highgui.h\""/"#include <opencv.hpp>"/g $x > _tmp
`cat _tmp > $x`
fi

nums=$(grep -iHn include\ \"ml.h $x|wc -l)
#nums=$(grep -iHn cv.h $x|wc -l)
if [ $nums -ne "0" ];
then
echo "$nums"
sed s/"#include \"ml.h\""/"#include <opencv.hpp>"/g $x > _tmp
`cat _tmp > $x`
fi

done
