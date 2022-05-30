echo "############################################################"
echo "##  Starting with user: "user1@feverup.com
echo
mkdir ~/bucket/user1@feverup
cd ~/bucket/user1@feverup
gsutil cp gs://bucket-id-here/object/name/user1-object1-here .
sleep 3
gsutil cp gs://bucket-id-here/object/name/user1-object2-here .
sleep 3
gsutil cp gs://bucket-id-here/object/name/user1-object3-here .
sleep 3
gsutil cp gs://bucket-id-here/object/name/user1-object4-here .
sleep 3
cd ~
sleep 10



echo "############################################################"
echo "##  Starting with user: "user2@feverup.com
echo
mkdir ~/bucket/user2@feverup
cd ~/bucket/user2@feverup
gsutil cp gs://bucket-id-here/object/name/user2-object1-here .
sleep 3
gsutil cp gs://bucket-id-here/object/name/user2-object2-here .
sleep 3
gsutil cp gs://bucket-id-here/object/name/user2-object3-here .
sleep 3
gsutil cp gs://bucket-id-here/object/name/user2-object4-here .
sleep 3
cd ~
sleep 10
