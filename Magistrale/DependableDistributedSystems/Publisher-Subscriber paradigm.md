we have both:
- **Publishers**: produce data in form of _events_
- **Subscribers**: declare interest on published data via a subscription, which is a filter on set of published events.
- **Event Notification Service**: Entity that notifies subscribers every published event that matches at least one of its subscriptions. It's also the mediator of the conversations between publishers and subscribers.
## Publish/Subscribe Model

The publish/subscribe (pub/sub) model is designed as a comprehensive solution to several communication challenges:
### Characteristics

1. **Many-to-Many Communication Model**  
   - Interactions occur in an environment where multiple information producers and consumers can communicate simultaneously.  
   - Each piece of information can be delivered to multiple consumers at the same time.  
   - Consumers can receive information from multiple producers.
2. **Space Decoupling**  
   - Interacting parties do not need to know each other.  
   - Message addressing is based on the content of the message.
3. **Time Decoupling**  
   - Interacting parties do not need to actively participate in the interaction at the same time.  
   - Information delivery is mediated through a third party.
4. **Synchronization Decoupling**  
   - Information flow from producers to consumers is mediated, eliminating the need for synchronization among interacting parties.
5. **Push/Pull Interactions**  
   - Both push and pull methods are supported for information delivery.
Depending on the subscription model we distinguish different flavors of pub/sub:
- **Topic based**: data published in the system is unstructured, apart from a tag identifying the topic. This is used by the ENS to route topics to the right subscribers.
- **Hierarchy based**: Topics, contrarily to the topic-based model, are structured hierarchically, with notion of containment between topics. When a subscriber subscribes to a topic, it implicitly subscribes to all subtopics
- **Content based selection**: All data is mostly structured, and each subscription is a set of constraints on attributes.

![[Pasted image 20250121123138.png]]