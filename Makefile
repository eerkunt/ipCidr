SHELL=bash
commands="192.168.0.1/24R" "192.168.0.0/24R" "192.168.0.256/24R!" "192.168.0.1/33R!" "192.168.0.2/255.255.255.0R" "192.168.0.2/255.255.256.0R!" "192.168.256.2/255.255.255.0R" "192.168.0.2-192.168.0.255R" "192.168.0.0-192.168.0.254R" "192.168.0.256-192.168.0.254R!"
EXECUTABLE=./ipCidr.py
FAILED=1

test:
	@chmod +x ${EXECUTABLE}
	@echo "Running tests."
	@testCount=0
	@FAILED=0
	@	for i in ${commands}; do										\
				CMD=`echo $${i} | cut -d "R" -f1`;					\
				RETURNCODE=`echo $${i} | cut -d "R" -f2`;		\
				let "testCount+=1"; \
				echo -n "Test #"; \
				echo -n $${testCount}; \
				echo ": Running with $${CMD} parameter. $${RETURNCODE}"; \
				$${RETURNCODE} ${EXECUTABLE} $${CMD} > /dev/null 2>&1; \
		 	done
	echo ${FAILED};
	@if [[ $${FAILED} -gt 0 ]]; then echo "$${FAILED} tests failed!"; exit 1; else echo "All tests successful. $${FAILED}"; exit 0; fi
