from create_job import create_job


def main():
    create = create_job()

    if not create:
        print(f"Create job failed!")
    else:
        print("Create job success!")


if __name__ == "__main__":
    main()
