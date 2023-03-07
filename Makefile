push:
	git add . && git commit -m "update" && git push

check:
	gh run list --workflow="ICR Image build and push" --limit 1

runjob:
	ibmcloud ce jobrun submit --name $$(date +%Y%m%d%H%M%S)-run  --job python-get-env