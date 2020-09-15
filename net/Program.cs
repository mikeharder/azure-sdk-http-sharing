using System;
using System.Diagnostics.Tracing;
using System.IO;
using System.Text;
using Azure.Storage.Blobs;

namespace httpsharing
{
    class Program
    {
        static void Main(string[] args)
        {
            var connectionString = Environment.GetEnvironmentVariable("STORAGE_CONNECTION_STRING");

            BlobClient client1 = new BlobClient(connectionString, "test", "test");
            Console.WriteLine("BlobClient.Upload #1");
            client1.Upload(Stream.Null, overwrite: true);

            BlobClient client2 = new BlobClient(connectionString, "test", "test");
            Console.WriteLine("BlobClient.Upload #2");
            client2.Upload(Stream.Null, overwrite: true);

            // Wireshark shows a single HTTPs connection was used for both requests
            //
            // TCP 64462 → 443[SYN] Seq = 0 Win = 64240 Len = 0 MSS = 1460 WS = 256 SACK_PERM = 1
            // TCP 443 → 64462[SYN, ACK] Seq = 0 Ack = 1 Win = 8192 Len = 0 MSS = 1440 WS = 256 SACK_PERM = 1
            // TCP 64462 → 443[ACK] Seq = 1 Ack = 1 Win = 263424 Len = 0
            // TLSv1.2 Client Hello
            // TCP 443 → 64462[ACK] Seq = 1 Ack = 199 Win = 262656 Len = 1460[TCP segment of a reassembled PDU]
            // TCP 443 → 64462[ACK] Seq = 1461 Ack = 199 Win = 262656 Len = 1460[TCP segment of a reassembled PDU]
            // TCP 443 → 64462[ACK] Seq = 2921 Ack = 199 Win = 262656 Len = 1460[TCP segment of a reassembled PDU]
            // TCP 64462 → 443[ACK] Seq = 199 Ack = 4381 Win = 263424 Len = 0
            // TLSv1.2 Server Hello, Certificate, Server Key Exchange, Server Hello Done
            // TCP 64462 → 443[ACK] Seq = 199 Ack = 5544 Win = 262144 Len = 0
            // TLSv1.2 Client Key Exchange, Change Cipher Spec, Encrypted Handshake Message
            // TLSv1.2 Change Cipher Spec, Encrypted Handshake Message
            // TLSv1.2 Application Data
            // TLSv1.2 Application Data
            // TLSv1.2 Application Data
            // TLSv1.2 Application Data
            // TCP 64462 → 443[RST, ACK] Seq = 1307 Ack = 6573 Win = 0 Len = 0
        }
    }
}
