# Exercise Week 4
## Ex 1
### a.
Easily enough, we can have the leader with only ch_a type, which we have assumed being perfect (not crash-prone) It'll send HEARTBEAT requests and will notify everyone in the case that a system hasn't answered, triggering also a _crash_ event.
### b.
Idea is to have two phases: every node sends HEARTBEAT requests through their channel_A links and waits $2\delta$ time for an ACK. If someone doesn't answer it'll send to every neighbor it has and will wait for its ACK, and in case send it back.
### c.
It's not, since we cannot be sure if a process didn't answer because of it being dead or if because message got lost (with probability $p_{drop} =  1 - p_{cons}$). We can create an eventually perfect failure detector $\Omega$.
## Ex 4
_using Perfect point to point links (pl) and perfect failure detector (f)_

**init**
	coordinator = get_coord()
	state = idle
	correct = $\Pi$

**upon event \<request>**
	state = waiting
	trigger <pl, send | REQUEST, coordinator>

**upon event \<pl, Deliver | \[GRANTED], coordinator>**
	state = CS

**upon event release()**
	state = idle
	trigget \<pl, send | REL, coordinator>

**upon event \<crash, p>**
	correct = correct \ {p}
	if p == coordinator
		coordinator = get_coord()
		if coordinator == self
			//Non lo so
			
# Exercise Week 5
## Ex 1
Will only write the added deliveries:
1. 
	p1: \[m1, m2, m3, m4, m5]
	p2: \[m5]
	p3: \[m1, m2, m3, m4]
2. 
	p1: \[m1, m2, m3, m4]
	p2: \[m5]
	p3: \[m1, m2, m3, m4]
3. 
	p1: \[m1, m2, m3, m4]
	p2: \[]
	p3: \[m1, m2, m3, m4]
## Ex 2
### 1
**quiescent uniform reliable broadcast**

**init**
	correct = $\Pi$
	ACK = $\emptyset$
	waiting = $\emptyset$
	sending = $false$
	

**upon event \<qurb, Broadcast | m >**
	waiting $\cup =$ {$m$}
	for every $p_i \in correct$
		trigger <fl, Send | \[MSG, m] , $p_i$>
	start_timer($\Delta$)

**upon timeout**
	for $m_i$ in waiting
		for all $p_i$ | $p_i \notin$ correct /  {$p_i | (m_i, p_i) \in ACK$}
			trigger <fl, Send | \[MSG, m], $p_i$>
	start_timer($\Delta$)

**upon event \<fl, Deliver | \[MSG, m], $p_i$>**
	if m not in waiting
		waiting $\cup =$ {$m$}
		for all $p_j \in correct$ | $p_j \neq p_i$
			trigger ,\<fl, Send | \[MSG, m], $p_j$>
		start_timer($\Delta$)
	ACK $\cup =$ {($m, p_j$)}
	trigger <fl, Send | \[ACK, m], $p_i$>

**upon event <fl, Deliver | \[ACK, m], $p_j$>**
	ACK $\cup =$ {($m, p_j$)}

**upon event \<f, Crash | ${p_i}$>**
	correct $/ =$ {$p_i$}
	remove all ACKs from $p_i$

**if exist $m_i$ $\in$ waiting | correct / {$p_i | (m_i, p_i) \in ACK$} = $\emptyset$**
	waiting /= {$m_i$}
	remove all ACKs for $m_i$
	trigger <qurb, Deliver | m>

### 2
Not without some more information

