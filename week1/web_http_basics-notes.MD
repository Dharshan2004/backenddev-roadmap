# Web & HTTP Basics

## Intro to the Internet

* The internet is a network of connected of computers
* Servers are computers which are directly connected to the internet
  * This makes our personal devices not servers but rather clients which make use of servers
* Each server have an IP address; these are rather not human readable and hence they have domain names
* Information sent over the internet are not sent as a whole; would be really slow and inefficient if done so
  * These information, such as files, emails and so on, are broken down into packets
  * Packets are then re-assembled in order at the destination
* Routers help route the packets to each of its destination

## HTTP

* Hypertext Transfer Protocol
* It is a application layer protocol; which means it is a higher level protocol
* This protocol allows web applications to communicate data and exchangfe data
* Based on TCP/IP Protocol
* Both the Server and Client have to communicate in the HTTP PRotocol
* Important things

  * Connectionless Protocol
    * The Connection is not persistent and uses a request-response model
    * HTTP can deliver any sort of data as long as the 2 computers are able to read and process it
    * HTTP is stateless; The 2 involved computers(server and client) are only aware of each other during the current request cycle
* Why HTTP?

  * Made to retrieve HTML files and hence designed for the web
  * Evolved to become to quickly and reliably move data on the internet
* Request-Response cycle

  * User types in the URL on their computer(client)
  * Client sends a HTTP message by connecting to the server over the internet and disconnect
  * Server recieves the request HTTP message, prepares a response and connects to the client and sends
    response message
* HTTP Message Structure

  * Start Line
  * Headers
  * Body
  * Usually all plaintext
  * Request Message
    * Start line
      * Method
        * Tells the server what it should do
        * GET, POST are examples
      * URI
      * Version
    * Headers
      * Are name value pairs
      * Adds rules
  * Response Message
    * Start Line
      * HTTP Version
      * Status Code
        * Ok 200
        * Error Codes
          * Example 404
* HTTP Status Code

  * 1xx - informational
  * 2xx - Success
  * 3xx - Redirect
  * 4xx - Client Error
  * 5xx - Server Error
  * Common Status Code
    * 200 - OK
    * 201 - OK created
    * 301 - Moved to new URL
    * 304 - Not Modifies (cached ver)
    * 400 - Bad Reques
    * 401 - Unauthorised
    * 404 - Not Found
    * 500 - Internal Server Error
* HTTP 2

  * Changes are more to do with efficiency on the background
  * Latency is reduced by enabling full request and response multiplexing
