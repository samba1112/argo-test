#!bin/bash
apt-get update -y
apt-get install -y libconfig-yaml-perl
value=$(perl -MYAML -le 'print YAML::LoadFile(shift)->{image}{tag}'  values.yaml)
sed -ie "s/tag: $value/tag: sample/g" values.yaml
