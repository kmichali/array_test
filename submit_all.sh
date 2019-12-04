for i in */*.pbs; do cd `dirname $i`; echo `pwd`; qsub `basename $i`; cd ..; done

