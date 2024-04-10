from create_job import create_job
import sys


def main():
    name = sys.argv[1]
    create = create_job(job_name=name)

    if not create:
        print(f"Create job failed!")
    else:
        print("Create job success!")


if __name__ == "__main__":
    main()
