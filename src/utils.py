from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def save_chunk_report(
    np_chunks,
    vp_chunks,
    output_file: str
) -> None:
    """
    Save chunk analysis results to a text file.
    """

    report_path = Path(output_file)

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "NLP CLASSIC TEXT ANALYSIS REPORT\n"
        )

        file.write("=" * 50)
        file.write("\n\n")

        file.write(
            "TOP NOUN PHRASE CHUNKS\n"
        )

        file.write("-" * 50)
        file.write("\n")

        for chunk, count in np_chunks:

            file.write(
                f"{count:>5} | {chunk}\n"
            )

        file.write("\n\n")

        file.write(
            "TOP VERB PHRASE CHUNKS\n"
        )

        file.write("-" * 50)
        file.write("\n")

        for chunk, count in vp_chunks:

            file.write(
                f"{count:>5} | {chunk}\n"
            )


def save_chunk_csv(
    chunks,
    output_file: str
) -> None:
    """
    Save chunk frequencies to CSV.
    """

    rows = []

    for chunk, count in chunks:

        rows.append(
            {
                "chunk": str(chunk),
                "count": count
            }
        )

    df = pd.DataFrame(rows)

    df.to_csv(
        output_file,
        index=False)

def save_frequency_chart(
    chunks,
    title: str,
    output_file: str,
    top_n: int = 10
) -> None:
    """
    Save a frequency chart for chunk counts.
    """

    top_chunks = chunks[:top_n]

    labels = [
        " ".join(
            word
            for word, tag in chunk
        )
        for chunk, count in top_chunks
    ]

    counts = [
        count
        for chunk, count in top_chunks
    ]

    plt.figure(figsize=(12, 6))

    plt.barh(
        labels[::-1],
        counts[::-1]
    )

    plt.title(title)

    plt.xlabel("Frequency")

    plt.tight_layout()

    plt.savefig(output_file)

    plt.close()