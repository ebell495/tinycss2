FROM python:3.8-bullseye
RUN pip3 install atheris

COPY . /tinycss2
WORKDIR /tinycss2
RUN python3 -m pip install . && chmod +x fuzz/tinycss2_fuzz.py

ENTRYPOINT [ ]
CMD ["/tinycss2/fuzz/tinycss2_fuzz.py"]