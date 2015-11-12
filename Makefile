SHELL=bash
commands="192.168.0.1/24R1" "192.168.0.0/24R3" "192.168.0.256/24R255" "192.168.0.1/33R-1" "192.168.0.2/255.255.255.0R1" "192.168.0.2/255.255.256.0R1" "192.168.256.2/255.255.255.0R1" "192.168.0.2-192.168.0.255R0" "192.168.0.0-192.168.0.254R0" "192.168.0.256-192.168.0.254R255"
EXECUTABLE=./ipCidr.py

test:
	chmod +x ${EXECUTABLE}
	@echo "Running tests."
	@ testCount=0
	@-	for i in ${commands}; do										\
				CMD=`echo $${i} | cut -d "R" -f1`;					\
				RETURNCODE=`echo $${i} | cut -d "R" -f2`;		\
				let "testCount+=1"; \
				echo -n "Test #"; \
				echo -n $${testCount}; \
				echo -n ": Running with $${CMD} parameter. Expected return code is $${RETURNCODE}..."; \
				${EXECUTABLE} $${CMD} > /dev/null 2>&1; if [ $$? -eq $${RETURNCODE} ]; then echo "Passed."; else  echo "Returned $$? ! Failed!"; exit -1; fi \
		 	done
	@echo "All tests successful."
