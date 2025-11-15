#!/usr/bin/env python3

"""
A minimal, short CLI chat app for LAN (Listener/Caller).

This script is a condensed version of the chat application.
- It hardcodes the port to 12345 for simplicity.
- It uses 'ascii' for encoding as requested.
- It fulfills the Listener(1st)/Caller(2nd) turn-based chat.
- It includes the required accept/decline functionality.
"""

import socket
import sys

def start_server():
    """Runs the Listener (Server) mode."""
    
    # Get a usable hostname/IP to display
    hostname = socket.gethostname()
    try:
        ip_addr = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_addr = "127.0.0.1" # Fallback
    
    PORT = 12345 # Hardcoded port for simplicity

    # Create and bind the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', PORT)) # Bind to all interfaces
    server_socket.listen(1)
    
    print(f"--- Listener Mode ---")
    print(f"Tell the caller to connect to:")
    print(f"  IP:   {ip_addr}")
    print(f"  Host: {hostname}")
    print(f"  Port: {PORT}")
    print("\nWaiting for a connection...")

    try:
        # Wait for a client
        conn, addr = server_socket.accept()
        print(f"\nConnection from: {addr[0]}:{addr[1]}")
        
        # Accept/Decline logic
        choice = input("Accept? (y/n): ").lower().strip()

        if choice == 'y':
            conn.sendall(b"ACCEPTED")
            print("Accepted. You speak first. (Ctrl+C to quit)\n")
            
            # --- Turn-based Chat Loop (Server starts) ---
            while True:
                # 1. Server speaks
                msg_out = input("You (Listener): ")
                conn.sendall(msg_out.encode('ascii'))
                
                # 2. Server listens
                msg_in = conn.recv(1024)
                if not msg_in:
                    print("\nClient disconnected.")
                    break
                print(f"Caller: {msg_in.decode('ascii')}")
        else:
            conn.sendall(b"REJECTED")
            print("Connection rejected.")
            conn.close()

    except KeyboardInterrupt:
        print("\nChat ended by server.")
    except socket.error as e:
        print(f"\nConnection error: {e}")
    finally:
        server_socket.close() # Clean up the server socket
        print("Server socket closed.")

def start_client():
    """Runs the Caller (Client) mode."""
    
    print("\n--- Caller Mode ---")
    HOST = input("Enter server IP or Hostname: ").strip()
    PORT = 12345 # Hardcoded port

    # Create and connect the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print(f"Connecting to {HOST}:{PORT}...")
        client_socket.connect((HOST, PORT))
        
        # Wait for server's response
        response = client_socket.recv(1024).decode('ascii')
        
        if response == "ACCEPTED":
            print("Connected! Wait for Listener. (Ctrl+C to quit)\n")
            
            # --- Turn-based Chat Loop (Client listens first) ---
            while True:
                # 1. Client listens
                msg_in = client_socket.recv(1024)
                if not msg_in:
                    print("\nServer disconnected.")
                    break
                print(f"Listener: {msg_in.decode('ascii')}")
                
                # 2. Client speaks
                msg_out = input("You (Caller): ")
                client_socket.sendall(msg_out.encode('ascii'))
        else:
            print("Server rejected the connection.")

    except KeyboardInterrupt:
        print("\nChat ended by client.")
    except (socket.error, ConnectionRefusedError) as e:
        print(f"\nConnection error: {e}")
    finally:
        client_socket.close() # Clean up the client socket
        print("Client socket closed.")

def main():
    """Main function to select mode."""
    try:
        mode = input("Choose mode: (1) Listen (2) Call: ").strip()
        if mode == '1':
            start_server()
        elif mode == '2':
            start_client()
        else:
            print("Invalid choice. Please run again and select 1 or 2.")
    except KeyboardInterrupt:
        print("\n\nExiting application.")
        sys.exit(0)

# Standard Python entry point
if __name__ == "__main__":
    main()