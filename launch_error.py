import subprocess

args = ['java',
        '-Xmx512m',
        '-Dtest.junit.threads=1',
        '-Dbuild.test.dir=/home/aoli/repos/zookeeper-4219/build/test/tmp',
        '-Dlog4j.configuration=file:/home/aoli/repos/zookeeper-4219/conf/log4j.properties',
        '-Dtest.data.dir=/home/aoli/repos/zookeeper-4219/build/test/data',
        '-Dzookeeper.DigestAuthenticationProvider.superDigest=super:D/InIHSb7yEEbrWz8b9l71RjZJU=',
        '-classpath',
        '/home/aoli/repos/zookeeper-4219/build/test/classes:/home/aoli/repos/zookeeper-4219/build/test/lib/antlr-2.7.7.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/antlr4-runtime-4.5.1-1.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/audience-annotations-0.5.0.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/checkstyle-6.13.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/commons-beanutils-1.9.2.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/commons-cli-1.2.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/commons-collections-3.2.2.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/commons-lang3-3.4.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/commons-logging-1.1.1.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/guava-18.0.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/hamcrest-core-1.3.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jackson-core-asl-1.9.11.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jackson-mapper-asl-1.9.11.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/javax.servlet-api-3.1.0.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jetty-http-9.2.18.v20160721.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jetty-io-9.2.18.v20160721.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jetty-security-9.2.18.v20160721.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jetty-server-9.2.18.v20160721.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jetty-servlet-9.2.18.v20160721.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jetty-util-9.2.18.v20160721.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/jline-2.11.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/junit-4.12.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/log4j-1.2.17.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/mockito-all-1.8.2.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/netty-3.10.5.Final.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/slf4j-api-1.7.5.jar:/home/aoli/repos/zookeeper-4219/build/test/lib/slf4j-log4j12-1.7.5.jar:/home/aoli/repos/zookeeper-4219/build/classes:/home/aoli/repos/zookeeper-4219/src/java/lib/ivy-2.4.0.jar:/usr/share/ant/lib/ant.jar:/usr/share/java/ant-launcher-1.10.7.jar:/usr/share/ant/lib/ant-junit.jar:/usr/share/ant/lib/ant-junit4.jar',
        'org.apache.tools.ant.taskdefs.optional.junit.JUnitTestRunner',
        'org.apache.zookeeper.server.quorum.CommitProcessorConcurrencyTest',
        'skipNonTests=false',
        'filtertrace=true',
        'haltOnError=false',
        'haltOnFailure=false',
        'formatter=org.apache.tools.ant.taskdefs.optional.junit.SummaryJUnitResultFormatter',
        'showoutput=true',
        'outputtoformatters=true',
        'logfailedtests=true',
        'threadid=0',
        'logtestlistenerevents=false',
        'formatter=org.apache.tools.ant.taskdefs.optional.junit.PlainJUnitResultFormatter,/home/aoli/repos/zookeeper-4219/build/test/logs/TEST-org.apache.zookeeper.server.quorum.CommitProcessorConcurrencyTest.txt', ]

subprocess.call(args)