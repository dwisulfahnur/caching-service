import argparse
import uvicorn

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default="127.0.0.1", help="The host address to bind to (default: 127.0.0.1)")
    parser.add_argument('--port', type=int, default=8000, help="The port to bind to (default: 8000)")
    parser.add_argument('--reload', action='store_true', default=True, help="Enable auto-reload (default: True)")
    parser.add_argument('--workers', type=int, default=1, help="Number of worker processes (default: 1)")

    args = parser.parse_args()

    uvicorn.run('src.main:app', host=args.host, port=args.port, reload=args.reload, workers=args.workers)
