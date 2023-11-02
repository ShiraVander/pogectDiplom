init:
	cd backend && \
	python -m venv venv && \
	pip install -r requirements.txt 
	

	cd desktop && \
	yarn

desk:
	cd desktop && yarn tauri dev

back:
	cd backend && \
	uvicorn app:app --reload