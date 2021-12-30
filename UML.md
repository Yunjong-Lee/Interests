# UML     
-. C to UML consideration:  
    +. C 파일 구조 = 클래스  
    +. C 파일 변수 = attribute 영역  
    +. C 파일 함수 = operation 영역  
    +. C 파일 매크로 = attribute 영역  
    +. C 파일 매크로 함수 = operation 영역  
    +. C 파일 헤더파일 = 클래스의 연관관계  
    +. C 파일 구조체(사용자정의) = 클래스의 inner 클래스로 표현  
  
  
  
#### Component Diagram  
(https://1000yun.tistory.com/8)  

- 시스템을 구성하는 SW의 조각, 임베디드 컨트롤러 등 조직과 종속성 표현
- class diagram보다 높은 수준의 추상화를 가지며, 하나 이상의 클래스에 의해 구현된다.

![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99512D335C73DEAF1E)  
그림. 구성 요소와 상호 관계의 수 예

어셈블리 커넥터는 주문에 의해 지정된 필요한 인터페이스 제품과 고객이 제공하는 인터페이스를 연결한다. 
종속 관계는 주문에 의해 지정된 필수 인터페이스 지불에 고객의 관련 계좌 정보를 매핑한다.



ref: https://developer.ibm.com/articles/the-sequence-diagram/

## Sequence Diagram

![img](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210803145028157.png)

그림 1. sequence diagram을 구성하는 주요 요소들

### Lifeline

  Lifetime은 다이어그램 상의 독립적인 참여자를 나타낸다. 2개 이상 다중으로 존재할 수 없는 각각이 단 하나의 상호작용 주체임

  symbol은 사각형(참여자 정보)에 수직선(참여자의 생명선)이 연결된 형태

![image-20210803145348728](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210803145348728.png)

  그림 2. Lifetime과 symbol

### Gate

  sequence diagram으로 보여지는 범위와 외부의 message에 대한 연결점으로, message에 대한 발신자와 수신자를 구체화

### Interaction Fragment

  해당 요소로 occurrence, execution, state invariant, combined fragment, interaction use가 있다.

![image-20210803151534161](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210803151534161.png)

![image-20210803151610689](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210803151610689.png)

![image-20210803151648137](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210803151648137.png)

![image-20210803151737261](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210803151737261.png)

 -. operator 종류:

![image-20210804145420163](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210804145420163.png)

  alt : switch와 유사, [...]가 guard condition으로 이 조건이 만족하면 해당하는Operand 부 수행( alt는 여러 옵션들이 있으므로 해당 guard condition에 따라서 수행되는 부분이 다르다)

  opt : if문과 같다.

  loop : operator에 반복 횟수를 (min, max) 혹은 (min..max)의 syntax로 적는다. 
		+. guard condition에 loop를 돌아야 하는 조건 기술
		+. break문은 guard condition이 참인 경우 해당 내용을 수행하고 현재 위치한 Fragment를 빠져 나간다. 
![image-20210803151822316](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210803151822316.png)

 ![image-20210803151852925](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210803151852925.png)





## state machine diagram

### Basic Concepts of State Machine Diagram

State machine diagram describes state-dependent behavior for an object.

### What is a State?

Rumbaugh defines that:

*"A state is an abstraction of the attribute values and links of an object. Sets of values are grouped together into a state according to properties that affect the gross behavior of the object."*

![State Notations](https://cdn-images.visual-paradigm.com/guide/uml/what-is-state-machine-diagram/02-state-notations.png)

​										그림. notations of state machine diagram

### Characteristics of State Machine Notations

There are several characteristics of states in general, regardless of their types:

- A state occupies an interval of time.
- A state is often associated with an abstraction of attribute values of an entity satisfying some condition(s).
- An entity changes its state not only as a direct consequence of the current input, but it is also dependent on some past history of its inputs.

### State

A state is a constraint or a situation in the life cycle of an object, in which a constraint holds, the object executes an activity or waits for an event.

![State Notation](https://cdn-images.visual-paradigm.com/guide/uml/what-is-state-machine-diagram/03-state-notation.png)

​												그림. Example of state machine diagram

#### Characteristics of State

- State represent the conditions of objects at certain points in time.
- Objects (or Systems) can be viewed as moving from state to state
- A point in the lifecycle of a model element that satisfies some condition, where some particular action is being performed or where some event is waited

### Initial and Final States

- The **initial state** of a state machine diagram, known as an initial pseudo-state, is indicated with a solid circle. A transition from this state will show the first real state
- The **final state** of a state machine diagram is shown as concentric circles. An open loop state machine represents an object that may terminate before the system terminates, while a closed loop state machine diagram does not have a final state; if it is the case, then the object lives until the entire system terminates.

Example:

![Start and Final State Example](https://cdn-images.visual-paradigm.com/guide/uml/what-is-state-machine-diagram/04-start-and-final-state-example.png)

​												그림. Example of initial and final states

### Events

An event signature is described as Event-name (comma-separated-parameter-list). Events appear in the internal transition compartment of a state or on a transition between states. An event may be one of four types:

1. Signal event - corresponding to the arrival of an asynchronous message or signal
2. Call event - corresponding to the arrival of a procedural call to an operation
3. Time event - a time event occurs after a specified time has elapsed
4. Change event - a change event occurs whenever a specified condition is met

#### Characteristics of Events

- Represents incidents that cause objects to transition from one state to another.
- Internal or External Events trigger some activity that changes the state of the system and of some of its parts
- Events pass information, which is elaborated by Objects operations. Objects realize Events
- Design involves examining events in a state machine diagram and considering how those events will be supported by system objects

### Transition

Transition lines depict the movement from one state to another. Each transition line is labeled with the **event** that causes the transition.

- Viewing a system as a set of states and transitions between states is very useful for describing complex behaviors

- Understanding state transitions is part of system analysis and design

- A Transition is the movement from one state to another state

- Transitions between states occur as follows:

  

  1. An element is in a source state
  2. An event occurs
  3. An action is performed
  4. The element enters a target state

- Multiple transitions occur either when different events result in a state terminating or when there are guard conditions on the transitions

- A transition without an event and action is known as automatic transitions

### Actions

Action is an executable atomic computation, which includes operation calls, the creation or destruction of another object, or the sending of a signal to an object. An action is associated with transitions and during which an action is not interruptible - e.g., entry, exit

### Activity

Activity is associated with states, which is a non-atomic or ongoing computation. Activity may run to completion or continue indefinitely. An Activity will be terminated by an event that causes a transition from the state in which the activity is defined

#### Characteristics of Action and Activities

- States can trigger actions
- States can have a second compartment that contains actions or activities performed while an entity is in a given state
- An action is an atomic execution and therefore completes without interruption
- Five triggers for actions: On Entry, Do, On Event, On Exit, and Include
- An activity captures complex behavior that may run for a long duration - An activity may be interrupted by events, in which case it does not complete occur when an object arrives in a state.

## Simple State Machine Diagram Notation

![Simple State Machine Diagram](https://cdn-images.visual-paradigm.com/guide/uml/what-is-state-machine-diagram/05-simple-state-machine-diagram.png)

### Entry and Exit Actions

Entry and Exit actions specified in the state. It must be true for every entry / exit occurrence. If not, then you must use actions on the individual transition arcs

- **Entry Action** executed on entry into state with the **notation: Entry / action**
- **Exit Action** executed on exit from state with the **notation: Exit / action**

#### Example - Entry / Exit Action (Check Book Status)

This example illustrates a state machine diagram derived from a Class - "BookCopy":

![Entry and Exit Actions](https://cdn-images.visual-paradigm.com/guide/uml/what-is-state-machine-diagram/06-entry-and-exit-actions.png)

Note:

1. This state machine diagram shows the state of an object myBkCopy from a BookCopy class
2. Entry action : any action that is marked as linked to the entry action is executed whenever the given state is entered via a transition
3. Exit action : any action that is marked as linked to the exit action is executed whenever the state is left via a transition

### Substates

A simple state is one which has no substructure. A state which has substates (nested states) is called a composite state. Substates may be nested to any level. A nested state machine may have at most one initial state and one final state. Substates are used to simplify complex flat state machines by showing that some states are only possible within a particular context (the enclosing state).

Substate Example - Heater

![Submachine Example](https://cdn-images.visual-paradigm.com/guide/uml/what-is-state-machine-diagram/07-submachine-example.png)

State Machine Diagrams are often used for deriving testing cases, here is a list of possible test ideas:

- Idle state receives Too Hot event
- Idle state receives Too Cool event
- Cooling/Startup state receives Compressor Running event
- Cooling/Ready state receives Fan Running event
- Cooling/Running state receives OK event
- Cooling/Running state receives Failure event
- Failure state receives Failure Cleared event
- Heating state receives OK event
- Heating state receives Failure event

### History States

Unless otherwise specified, when a transition enters a composite state, the action of **the nested state machine starts over again at the initial state** (unless the transition targets a substate directly). History states allow the state machine to **re-enter the last substate that was active prior to leaving** the composite state. An example of history state usage is presented in the figure below.

![History of State Machine Example](https://cdn-images.visual-paradigm.com/guide/uml/what-is-state-machine-diagram/08-history-state-example.png)

### Concurrent State

As mentioned above, states in state machine diagrams can be nested. Related states can be grouped together into a single composite state. Nesting states inside others is necessary when an activity involves concurrent sub-activities. The following state machine diagram models an auction with two concurrent substates: processing the bid and authorizing the payment limit.

Concurrent State Machine Diagram Example - Auction Process

In this example, the state machine first entering the Auction requires a fork at the start into two separate start threads. Each substate has an exit state to mark the end of the thread. Unless there is an abnormal exit (Canceled or Rejected), the exit from the composite state occurs when both substates have exited.

![Concurrent State Machine Example](https://cdn-images.visual-paradigm.com/guide/uml/what-is-state-machine-diagram/09-concurrent-state-machine-example.png)

