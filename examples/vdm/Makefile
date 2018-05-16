# See README.txt.

.PHONY: all cpp java python clean

all: python

cpp:    add_person_cpp    vdm_cpp
go:     add_person_go     vdm_go
gotest: add_person_gotest vdm_gotest
java:   add_person_java   vdm_java
python: vdm_python

clean:
	rm -f vdm_python
	rm -f javac_middleman AddPerson*.class ListPeople*.class com/example/tutorial/*.class
	rm -f protoc_middleman vdm_pb2.py
	rm -f *.pyc
	rm -rf __pycache__

protoc_middleman: vdm.proto
	protoc $$PROTO_PATH --python_out=. vdm.proto
	@touch protoc_middleman

vdm_cpp: vdm.cc protoc_middleman
	pkg-config --cflags protobuf  # fails if protobuf is not installed
	c++ vdm.cc addressbook.pb.cc -o vdm_cpp `pkg-config --cflags --libs protobuf`

vdm_python: vdm.py protoc_middleman
	@echo "Writing shortcut script vdm_python..."
	@echo '#! /bin/sh' > vdm_python
	@echo './vdm.py "$$@"' >> vdm_python
	@chmod +x vdm_python
