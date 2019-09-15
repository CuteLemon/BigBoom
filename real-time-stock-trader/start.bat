cd ../kafka/kafka-docker
docker-compose -f docker-compose-single-broker.yml up -d

cd ..
cd ..
cd ./spark/docker-spark
docker-compose up -d