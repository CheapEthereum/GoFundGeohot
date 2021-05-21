async function main() {

    const [deployer] = await ethers.getSigners();

    console.log(
      "Deploying contracts with the account:",
      deployer.address
    );

    console.log("Account balance:", (await deployer.getBalance()).toString());

    const Token = await ethers.getContractFactory("GoFundGeohot");
    const token = await Token.deploy("0x9485678eeE750D71479D3a993D2F3DD8c8B083D3");

    console.log("Token address:", token.address);
  }

  main()
    .then(() => process.exit(0))
    .catch(error => {
      console.error(error);
      process.exit(1);
    });
