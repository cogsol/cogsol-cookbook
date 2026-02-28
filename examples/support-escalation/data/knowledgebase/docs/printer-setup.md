# Printer Setup and Troubleshooting

Guide for adding printers and resolving common printing problems.

## Adding a Network Printer

1. Open Settings > Devices > Printers and Scanners.
2. Click "Add a printer or scanner".
3. If the printer appears in the list, select it and click "Add device".
4. If not found, click "The printer I want isn't listed".
5. Select "Add a printer using a TCP/IP address" and enter the printer IP.
6. Standard printer IPs follow the format 10.1.FLOOR.PRINTER (e.g. 10.1.2.101 for Floor 2, Printer 1).

## Common Printer Names

- HQ-2F-PRINTER-01: Headquarters, 2nd Floor, Color Laser
- HQ-3F-PRINTER-01: Headquarters, 3rd Floor, Color Laser
- WC-GF-PRINTER-01: West Campus, Ground Floor, B&W Laser

## Print Job Stuck in Queue

1. Open Services (search "services" in Start menu).
2. Find "Print Spooler", right-click and select "Stop".
3. Open File Explorer and navigate to C:\Windows\System32\spool\PRINTERS.
4. Delete all files in that folder.
5. Go back to Services and Start the Print Spooler service.
6. Retry your print job.

## Printer Shows Offline

- Check that the printer is powered on and connected to the network.
- On your computer, go to Printers and Scanners, click the printer, and select "Open queue".
- Uncheck "Use Printer Offline" if it is checked.
- Restart both the printer and your computer.

## Scan to Email

Most network printers support scan to email. Place your document in the feeder, select "Scan to Email" on the printer display, enter your email address, and press Start. The scan will arrive in your inbox within a few minutes.
