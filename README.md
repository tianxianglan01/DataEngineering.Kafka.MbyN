# DataEngineering.Kafka.MbyN
use Kafka to build a M-input and N-output pipeline.


You need to create a data pipeline where data flows in from Producers and get sent out to Consumers.
Expect to create M (where M > 3) Producers (extra credit for creating each Producer in a different language or source type) and N (where N > 5) Consumers which can do something with the data produced by the Producers.

Also, there should be two or more Topics within Kafka.

And yes, It's okay to spin up 5 of Producer1, etc and 4 of Consumer2 and so on. (This mean you'll have several copies running of each Producer and Consumer. They can be written in python, Java, SQL or any other implementation.

Use [Event Streaming Introduction](https://medium.com/swlh/introduction-to-event-streaming-with-kafka-and-kafdrop-22afdb4b380a) for info on how to get kafka and kafdrop running in a docker container.

Then, write each producer and consumer, and attach them to the DOCKER container.

Be sure to describe in an "Architecture.md" file what your Producers and Consumers do (what data they handle, where they get it from or send it to). Make a decision about which libraries you'll use to create Producers/consumers in either Python or Java or from a SQL script. (or other sources of data).

More References

- [Kafka Intro](https://medium.com/better-programming/an-introduction-to-apache-kafka-95a82260c1c3)
- [Kafka: Python](https://towardsdatascience.com/getting-started-with-apache-kafka-in-python-604b3250aa05)
- [Kafka Battles](https://medium.com/@stephane.maarek/the-kafka-api-battle-producer-vs-consumer-vs-kafka-connect-vs-kafka-streams-vs-ksql-ef584274c1e)

### But Perhaps...

You should think about *how do I create a producer in python, something that __generates__ data, possibly random, in an unlimited fashion?*

A __generator__ in python can create things without building a big memory foot print? rememeber? Feel free to share your ideas on how to do this within the cohort, the main idea of this lab is *Kafka* not *python*, so if some of you come up with cool little data generators, __share them within the cohort__.
