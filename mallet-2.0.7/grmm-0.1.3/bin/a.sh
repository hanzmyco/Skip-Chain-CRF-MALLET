java -cp ../class:../lib/mallet-deps.jar:../lib/grmm-deps.jar \
edu.umass.cs.mallet.grmm.learning.GenericAcrfTui \
--training featuretrain.txt \
--testing featuretest.txt \
--model-file tmpls.txt > xu_out_skip.txt 2> xu_err_skip.txt
