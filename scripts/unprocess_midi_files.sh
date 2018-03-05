if [ ! -d ../data/unprocessed ]; then
    mkdir ../data/unprocessed
fi
if [ ! -d ../data/generated ]; then
    mkdir ../data/generated
fi
python ../lib/unsimplify_midi.py
for filename in ../data/unprocessed/*.csv
    do csvmidi $filename >> $filename.mid
    mv ../data/unprocessed/*.mid ../data/generated
done