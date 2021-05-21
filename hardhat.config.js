require("@nomiclabs/hardhat-waffle");
require("hardhat-gas-reporter");

var fs = require('fs');
const home = require('os').homedir();
const keyfile = require('path').join(home, '.key')
var goFundGeoKey = fs.readFileSync(keyfile, { encoding: 'utf8' });

/**
 * @type import('hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: {
    version: "0.8.0",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200
      }
    }
  },
  networks: {
    cheapeth: {
      url: "https://rpc.cheapeth.org/rpc",
      accounts: [goFundGeoKey],
      gasPrice: 2000000000
    }
  },
  paths: {
    sources: "./contracts",
    tests: "./test",
  },
};
