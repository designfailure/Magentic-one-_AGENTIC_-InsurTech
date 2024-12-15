import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--interface', type=str, choices=['gradio', 'streamlit'], 
                       default='gradio', help='Izbira uporabniškega vmesnika')
    args = parser.parse_args()
    
    if args.interface == 'gradio':
        from gradio_app import create_interface
        app = create_interface()
        app.launch(share=True)
    else:
        import streamlit.cli as stcli
        import sys
        sys.argv = ["streamlit", "run", "streamlit_app.py"]
        stcli.main()

if __name__ == "__main__":
    main() 