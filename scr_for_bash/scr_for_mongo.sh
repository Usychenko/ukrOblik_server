#! /bin/bash
python3 ~/mq-test/mongo/insert_meter.py
for f in $(ls ~/mq-test/some_json/engel)
do

if test $f != 'engel_done'; then
    mv ~/mq-test/somo_json/engel/$f   ~/mq-test/somo_json/engel/engel_done/$f
fi
done

