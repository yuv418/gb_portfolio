# Projects

Here's a list of recent (semi-noteworthy) programming projects that I've worked on (everything else is available on GitHub/GitLab):

**[vGPU Streaming (mostly finished)](https://github.com/yuv418/echodawn)**: I've mostly finished a project that captures the buffer of an NVIDIA vGPU running in a KVM virtual machine and streams the buffer over the network by encoding the buffer into a video stream, allowing a remote desktop servers that runs on a VM host instead of the guest. It uses the `libav*` family of libraries, and a custom TCP protocol using Protocol Buffers to send mouse and keyboard data. 

**[MQA Player (finished)](https://github.com/yuv418/libbluos_ssc_ipc)**: I used a shared library for a DAC that was an armv7 machine running embedded Linux and existing code that called aforementioned library, but expanded on it to make an IPC system to decode MQA on-the-fly from an x86 executable, which involved implementing my own mutexes and semaphores and learning how to use shared memory.

**[emotes-rs](https://github.com/yuv418/emotes-rs)**: When you chat on Discord and paste the link to an image, Discord will remove the link and you'll only see the image. I thought it would be cool if you come up with memorable URLs that return images that are the size of emojis, allowing you send custom "emojis" in Discord. The Rust backend I wrote exposes a GraphQL API (using the wonderful async-graphql library) to manage users and uploading emotes, that uses SQLx to communicate to a PostgreSQL database. It also utilizes libvips to resize images quickly (resizing GIF emotes can be quite expensive and this library is exceedingly performant). I also wrote a version of this application in Python which was somewhat more featured, but it became impossible to maintain since I used too many niche libraries that were poorly documented. A frontend for emotes-rs using Svelte is also available.

Here's a picture of my code (for the first project) I took for fun!

![Picture of my code](assets/codemonitors.jpeg "Picture of my code")
