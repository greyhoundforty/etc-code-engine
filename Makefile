turbo-mode: push watch 

watch: gh-run-watch ce-submit-job

push:
	git add . && git commit -m "update" && git push

gh-run-list:
	gh run list --workflow="ICR Image build and push" --limit 1

gh-run-watch:
	gh run watch && echo "run is done!"

# Submit new job run to Code Engine
ce-submit-job:
	echo "Submitting job run to Code Engine"
	
	ibmcloud ce jobrun submit --name $$(date +%Y%m%d%H%M%S)-run  --job python-get-env 

	echo "Following jobrun logs" 

	ibmcloud ce jobrun logs -f -n $$(ibmcloud ce jobrun list -s age --job python-get-env --output json | jq -r '.items[0].metadata.name')

