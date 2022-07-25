# Music Source Separation

## Endpoint
Run python script with dedicated port (default `5000`)
```shell
python endpoint.py --port=PORT_NUMBER
```
Send `POST` request to `http://127.0.0.1:PORT_NUMBER/separate`, available arguments:
* `file` - path to input sound.
* `model` (*optional*, default `mdx_extra_q`) - name of  the model that is going to be used:
    * `mdx` - trained only on MusDB HQ, winning model on track A at the MDX challenge.
    * `mdx_extra` - trained with extra training data (including MusDB test set), ranked 2nd on the track B of the MDX challenge.
    * `mdx_q`, `mdx_extra_q` - quantized version of the previous models. Smaller download and storage but quality can be slightly worse. `mdx_extra_q` is the default model used.
    * `SIG`: where `SIG` is a single model from the model zoo.
* `jobs` (*optional*, default `1`) - number of parallel jobs
### Output Example
```json
{
    "inference_time": 18.026292085647583,
    "bass": "/Users/pat/dev/music-source-separation/output/mdx_q/test/bass.wav",
    "drums": "/Users/pat/dev/music-source-separation/output/mdx_q/test/drums.wav",
    "other": "/Users/pat/dev/music-source-separation/output/mdx_q/test/other.wav",
    "vocals": "/Users/pat/dev/music-source-separation/output/mdx_q/test/vocals.wav"
}
```

## References
1. [Transcription is All You Need: Learning to Separate Musical Mixtures with Score as Supervision](https://arxiv.org/pdf/2010.11904.pdf)
2. [Music Source Separation in the Waveform Domain](https://arxiv.org/pdf/1911.13254.pdf)
3. [Simultaneous Separation and Transcription of Mixtures with Multiple Polyphonic and Percussive Instruments](https://arxiv.org/pdf/1910.12621.pdf)
4. [Towards Automatic Instrumentation by Learning to Separate Parts in Symbolic Multitrack Music](https://arxiv.org/pdf/2107.05916.pdf)
