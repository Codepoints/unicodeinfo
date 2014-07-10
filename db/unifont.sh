#!/bin/bash

TARGET=images.sql
NOCP=

cd $(dirname $0)
true > $TARGET
mkdir /tmp/cp
for u in ../data/unifont/uni????.png; do
  echo Processing $u
  z=$(basename $u .png)
  z=${z:3}
  if [[ ${z:0:2} == "00" ]]; then
    z=${z:2}
  fi
  for a in $(seq 0 15); do
    ax=$(echo 'ibase=10;obase=16;'"$a" | bc)
    for b in $(seq 0 15); do
      bx=$(echo 'ibase=10;obase=16;'"$b" | bc)
      let x=64+8+a*32
      let y=32+7+b*32
      F="$z$ax$bx"
      echo -n "U+$F"
      convert $u -crop 16x16+$x+$y -geometry 16x16+0+0 \
          +repage \
          -gravity West -background red -splice 1x0 \
          -trim +repage \
          -gravity Center \
          -extent 16x16 \
          -transparent white \
          -transparent red \
          +repage \
          "/tmp/cp/U+$F.tmp.png"
      optipng -quiet -o7 "/tmp/cp/U+$F.tmp.png"
      pngcrush -q -rem alla "/tmp/cp/U+$F.tmp.png" "/tmp/cp/U+$F.png"
      /bin/rm "/tmp/cp/U+$F.tmp.png"
      echo 'INSERT INTO codepoint_image (cp, image) VALUES (' $((0x$F)) ", '"$(base64 -w 0 "/tmp/cp/U+$F.png")"');" >> $TARGET
      # new Unifont versions have no generic "no cp" image :-(
      #if [[ $ax$bx == FFF8 ]]; then
      #  # This is a (hopefully) not assigned codepoint. Later we
      #  # will erase all lines with this image
      #  NOCP=$(base64 -w 0 "/tmp/cp/U+$F.png")
      #fi
      /bin/rm "/tmp/cp/U+$F.png"
      echo -n -e "\b\b"
      for Q in $(seq ${#F}); do echo -n -e '\b'; done
    done
  done
done
rmdir /tmp/cp
if [[ $NOCP ]]; then
  NOCP=$(echo "$NOCP" | sed -e 's/\([[\/.*]\|\]\)/\\&/g')
  sed -i "/$NOCP/d" $TARGET
fi
exit 0

