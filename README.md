# Glaive Streaming

Glaive is a very simple framework for easily creating streaming applications.
The application uses `pickle` and Python 3. Each operator consists of a simple
Python script that reads data and can emit tuples.

The `glaive.sh` function can be used as an interface to call operators and construct
streams. The intention of Glaive is to return to the roots of shell scripting and the
original Linux philosophy of placing configuration in environment variables and command line
parameters, where each script performs a simple function and the output is neutral and
can be parsed by another script by using Unix pipes to redirect stdin and stdout.

Therefore, Glaive streams are linear and at the basic level do not support branching,
though the framework can in theory support it.

The `samples/` directory contains two operators: `beacon.py` and `dump.py`. These can be
connected by calling the following in `bash`:

```
glaive samples/beacon period=10 | glaive samples/dump
```

The Python package will cache the values of stdin and stdout. `print()` calls will be redirected
to stderr, and `glaive` will handle the receipt of tuples from stdin and their submission on stdout.
