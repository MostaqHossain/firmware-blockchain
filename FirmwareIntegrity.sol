// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FirmwareIntegrity {
    mapping(string => string) private firmwareHashes;

    function storeFirmwareHash(string memory deviceID, string memory hash) public {
        firmwareHashes[deviceID] = hash;
    }

    function getFirmwareHash(string memory deviceID) public view returns (string memory) {
        return firmwareHashes[deviceID];
    }
}