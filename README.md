[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/YonLiud/Israeli-Queue">
    <img src="https://i.ibb.co/bgJQ792/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Israeli Queue</h3>

  <p align="center">
    A variation of Priority Queues where the priority of elements can change dynamically based on their relationships with other elements in the queue
 </p>

</p>

## About Israeli Queue
Israeli Queues are a playful take on this real-world behavior, where the priority of elements in the queue is influenced not only by their inherent priority but also by their relationships to other elements already in the queue. This results in a more complex and realistic simulation of how queues might work in certain social contexts.

### Key Characteristics:

* Dynamic Priority: Unlike traditional priority queues where each element has a fixed priority, in Israeli Queues, the priority can change based on the position and relationship with other elements in the queue.
* Group Influence: Elements can be grouped, and elements within the same group may join each other, altering the order of the queue.
* Real-World Simulation: This algorithm provides a closer approximation to real-world scenarios where social relationships and behaviors affect queuing order.

### Applications:
1. Event Management: Israeli Queues can be used in event management systems where attendees might have VIP passes or group entries that allow them to join the queue at different points.
2. Customer Service: In customer service scenarios, regular customers or members of loyalty programs might receive different queuing treatment.
3. Simulation and Modeling: This concept can be used in simulations that require a more nuanced approach to queuing, reflecting human social behaviors.
<!-- GETTING STARTED -->
## Getting Started

To get the module working simply follow these steps:

### Installation

```sh
pip install IsraeliQueue
```


<!-- USAGE EXAMPLES -->
## Usage Example

#### Sort by `Key`

<a href="https://ibb.co/2kbWsKQ"><img src="https://i.ibb.co/kSd59cf/carbon-1.png" alt="carbon-1" border="0"></a>

Returns: `[Item(item='Noy', group=0), Item(item='Nitzan', group=0), Item(item='Omry', group=1), Item(item='Omer', group=1), Item(item='Oz', group=1), Item(item='Alma', group=2)]`


#### Sort by `Type`

<a href="https://ibb.co/3dW9m08"><img src="https://i.ibb.co/yP5cF8M/carbon-2.png" alt="carbon-2" border="0"></a>

Returns: `[[2, 4], ['Alex', 'Robert'], [[0.4, 0.9]]]`

<!-- ROADMAP 
## Roadmap

See the [open issues](https://github.com/YonLiud/Israeli-Queue/issues) for a list of proposed features (and known issues).
-->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Links

* Project Link: [https://github.com/YonLiud/Israeli-Queue](https://github.com/YonLiud/Israeli-Queue)
* PyPI Link:    [https://pypi.org/project/IsraeliQueue/](https://pypi.org/project/IsraeliQueue/)

<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/YonLiud/Israeli-Queue.svg?style=for-the-badge
[contributors-url]: https://github.com/YonLiud/Israeli-Queue/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/YonLiud/Israeli-Queue.svg?style=for-the-badge
[forks-url]: https://github.com/YonLiud/Israeli-Queue/network/members
[stars-shield]: https://img.shields.io/github/stars/YonLiud/Israeli-Queue.svg?style=for-the-badge
[stars-url]: https://github.com/YonLiud/Israeli-Queue/stargazers
[issues-shield]: https://img.shields.io/github/issues/YonLiud/Israeli-Queue.svg?style=for-the-badge
[issues-url]: https://github.com/YonLiud/Israeli-Queue/issues
[license-shield]: https://img.shields.io/github/license/YonLiud/Israeli-Queue.svg?style=for-the-badge
[license-url]: https://github.com/YonLiud/Israeli-Queue/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/YonLiud
