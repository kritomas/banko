# Banqo - Usage

This document goes into deeper details about Banqo's capabilities.

The application has a command line interface, split into modes. At any time, you can type `help` for a list of available commands, or `exit` to exit the current mode (that means exiting the application in global mode). Signaling EOF (CTRL+D on POSIX systems) also invokes `exit`.

## Global mode

Prompt:

```
: 
```

The global mode's serves as a junction to access all the other modes.

## Account mode

Prompt:

```
account: 
```

This mode is for managing accounts. It can open accounts, close accounts, deposit/withdraw money from accounts. It cannot transfer money between accounts, we have the transaction mode for that.

## Bank mode

Prompt:

```
bank: 
```

This mode is for managing banks. It also supports bank import from CSV files. The CSV must be in the following format:

```
city,street,house_number,additional_address_info_(can_be_blank)
```

## Client mode

Prompt:

```
client: 
```

This mode is for managing clients. It also supports client import from CSV files. The CSV must be in the following format:

```
first_name,last_name,email,city,street,house_number,additional_address_info_(can_be_blank)
```

## Transaction mode

Prompt:

```
transaction: 
```

This mode is for transferring money between accounts.