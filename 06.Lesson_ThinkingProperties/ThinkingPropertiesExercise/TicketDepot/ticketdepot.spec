methods {
    getRemainingTicket(uint16 eventId) returns (uint16) envfree
    getTicketPrice(uint16 eventId) returns (uint64) envfree
    getEventOwner(uint16 eventId) returns (address) envfree
}

rule ticketsRemainingMonotonousDecrease(method f, uint16 eventId) {
    require eventId != 0;

    uint16 ticketRemaining_before = getRemainingTicket(eventId);
    
    env e;
    calldataarg args;
    f(e,args);

    uint16 ticketRemaining_after = getRemainingTicket(eventId);

    assert ticketRemaining_after == ticketRemaining_before - 1 => f.selector == buyNewTicket(uint16, address).selector || ticketRemaining_after == ticketRemaining_before;
} 


rule ticketsPriceCanNotBeDecreased(method f, uint16 eventId) {
    require eventId != 0;

    uint16 ticketPrice_before = getPriceTicket(eventId);
    
    env e;
    calldataarg args;
    f(e,args);

    uint16 ticketPrice_after = getPriceTicket(eventId);

    assert ticketPrice_after == ticketPrice_before;
} 

rule numEventMonotonousIncrease(method f) {
    uint16 numEvent_before = getTotalNumberOfEvents();
    
    env e;
    calldataarg args;
    f(e,args);
 
    uint16 numEvent_after = getTotalNumberOfEvents();
    assert numEvent_after = numEvent_before + 1 => f.selector == function createEvent(uint64, uint16).selector || numEvent_after == numEvent_before;
} 



 