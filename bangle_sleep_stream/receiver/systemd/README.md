# systemd directory overview

## Purpose

Contains the Linux service unit used to run the receiver daemon on boot.

## Files and fit

- sleepstream-receiver.service: process lifecycle config (restart policy, working directory, startup command).

## Control flow

systemd starts the receiver at boot, restarts it on failures, and keeps it running unattended.
