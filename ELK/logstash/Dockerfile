FROM logstash:7.3.1

RUN rm -rf /usr/share/logstash/pipeline/logstash.conf
ADD ./elk-demo-logstash.conf /usr/share/logstash/pipeline/
# ADD ./logstash.conf /usr/share/logstash/pipeline/