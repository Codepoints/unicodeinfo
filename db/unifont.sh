#!/bin/bash

TARGET=images.sql
NOCP=

cd $(dirname $0)
true > $TARGET
mkdir /tmp/cp
for u in ../data/unifont/uni??.bmp; do
  break
  echo Processing $u
  z=$(basename $u .bmp)
  z=${z:3}
  for a in $(seq 0 15); do
    ax=$(echo 'ibase=10;obase=16;'"$a" | bc)
    for b in $(seq 0 15); do
      bx=$(echo 'ibase=10;obase=16;'"$b" | bc)
      let x=64+8+a*32
      let y=32+7+b*32
      F="U+$z$ax$bx"
      echo -n "$F"
      convert $u -crop 16x16+$x+$y -geometry 16x16+0+0 \
          +repage \
          -gravity West -background red -splice 1x0 \
          -trim +repage \
          -gravity Center \
          -extent 16x16 \
          -transparent white \
          -transparent red \
          +repage \
          "/tmp/cp/U+$z$ax$bx.tmp.png"
      pngcrush -q -rem alla "/tmp/cp/U+$z$ax$bx.tmp.png" "/tmp/cp/U+$z$ax$bx.png"
      /bin/rm "/tmp/cp/U+$z$ax$bx.tmp.png"
      echo 'INSERT INTO codepoint_image (cp, image) VALUES (' $((0x$z$ax$bx)) ", '"$(base64 -w 0 "/tmp/cp/U+$z$ax$bx.png")"');" >> $TARGET
      if [[ $ax$bx == FFF8 ]]; then
        # This is a (hopefully) not assigned codepoint. Later we
        # will erase all lines with this image
        NOCP=$(base64 -w 0 "/tmp/cp/U+$z$ax$bx.png")
      fi
      /bin/rm "/tmp/cp/U+$z$ax$bx.png"
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

