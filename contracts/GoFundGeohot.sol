// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeMath.sol";

//
// On 5/19/20, @geohot affirmed he would implement Checkpointing for Cheap
// if given 20k cTH:
//   https://discord.com/channels/808222539108188200/811270603431477258/844802655964758018
//
// This contract is a crowd funding to hire Geohot for the job.
// The logic will be:
//   - anyone can chip in using donate()
//   - anyone can withdraw their donation while the
//     contract is still pending undonate()
//   - only geohot can withdraw the funds using:
//     iAmGeoHotAndICommitToDeliverCheckpointingToCheapETH()
//   - geohot can only withdraw if the 20k target is met.  And
//     he will get all the funds, possibly more than 20k
//
contract GoFundGeohot {

    using SafeMath for uint256;

    string public name = "Go Fund Geohot";
    string public symbol = "GFG";

    // This address only can withdraw funds
    address public _beneficiary;

    // Each donator balance
    mapping(address => uint256) _donatorBalances;

    constructor(address beneficiary) {
        // Geohot is 0x9485678eeE750D71479D3a993D2F3DD8c8B083D3
        _beneficiary = beneficiary;
    }

    // geohot can use this to change his address
    function setBeneficiary(address newBeneficiary) external {
        require(_beneficiary == msg.sender, "Only the current beneficiary can change the beneficiary");
        _beneficiary = newBeneficiary;
    }

    // retreive the beneficiary address
    function getBeneficiary() external view returns (address) {
        return _beneficiary;
    }

    // please donate to the cheap ETH cause
    function donate() external payable {
        _donatorBalances[msg.sender] = _donatorBalances[msg.sender].add(msg.value);
    }

    // in case you change your mind and wants to get your money back
    function unDonate(uint256 amount) external {
        require(_donatorBalances[msg.sender] >= amount,
                "Cannot withdraw that much");

        // Transfer the amount.
        _donatorBalances[msg.sender] = _donatorBalances[msg.sender].sub(amount);
        payable(msg.sender).transfer(amount);
    }

    // retreive a donator balance
    function getBalance(address donator) external view returns (uint256) {
        return _donatorBalances[donator];
    }

    // geohot: your turn
    function iAmGeoHotAndICommitToDeliverCheckpointingToCheapETH() external {
        require(_beneficiary == msg.sender, "You are not Geohot! Imposter!");
        require(address(this).balance >= 20000 ether, "The contract doesn't have enough cheapETH to execute");

        selfdestruct(payable(msg.sender));
    }
}
