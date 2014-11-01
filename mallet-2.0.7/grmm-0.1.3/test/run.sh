java -cp $GRMM/class:$GRMM/lib/mallet-deps.jar:$GRMM/lib/grmm-deps.jar \ edu.umass.cs.mallet.grmm.learning.GenericAcrfTui \ --training $GRMM/test/grmm/conll2000.train1k.txt \
    --testing  $GRMM/test/grmm/conll2000.test1k.txt \
    --model-file tmpls.txt > stdout.txt 2> stderr.txt