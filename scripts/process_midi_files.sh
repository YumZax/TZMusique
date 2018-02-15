if [ ! -d ../data/processed ]; then
    mkdir ../data/processed
fi

for filename in ../data/*.mid
    do midicsv $filename >> $filename.csv
    mv ../data/*.csv ../data/processed
done

#TODO : Adapt those csv files to make them have simpler data