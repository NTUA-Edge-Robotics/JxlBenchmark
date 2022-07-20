#!/bin/bash

dir=$(dirname $0);

echo "method,image,error,size,pixels,enc_speed,dec_speed,bpp,dist,psnr,p,bppp,qabpp";

for image in $1; do
    for distance in 0 1 1 1.9 2.8 3.7 4.6 5.5; do
        for effort in lightning thunder falcon cheetah hare wombat squirrel kitten; do
            output=$(cjxl $image -d $distance -e $effort --num_reps 10 2>&1);
            image_name=$(basename $image);

            echo -n "jxl:$effort:d$distance,";
            echo -n $image_name;
            echo -n ",0,";
            python3 $dir/extract_data_from_cjxl_output.py "$output";
        done
    done
done
