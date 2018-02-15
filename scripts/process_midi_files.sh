for filename in ../data/*.mid
do midicsv $filename >> $filename.csv
mv ../data/*.csv ../data/processed
done